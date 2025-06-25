
import pandas as pd
import sqlite3

# Connect to the Chinook database
conn = sqlite3.connect('chinook.db')

# Load necessary tables
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices = pd.read_sql_query("SELECT CustomerId, Total FROM invoices", conn)
invoice_items = pd.read_sql_query("SELECT InvoiceId, TrackId FROM invoice_items", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM tracks", conn)

#------------------------------
#Task 1: Customer Purchases Analysis
#------------------------------

#1. Calculate total amount spent by each customer
customer_totals = invoices.groupby('CustomerId')['Total'].sum().reset_index(name='TotalSpent')

#2. Top 5 customers by amount spent
top5_customers = customer_totals.sort_values(by='TotalSpent', ascending=False).head(5)

#3. Join with customer names
top5_customers = top5_customers.merge(customers, on='CustomerId')
top5_customers = top5_customers[['CustomerId', 'FirstName', 'LastName', 'TotalSpent']]

print("Top 5 Customers by Purchase Amount:\n")
print(top5_customers)

# ------------------------------
#Task 2: Album vs. Individual Track Purchases
# ------------------------------

# Step 1: Merge invoice_items with tracks to get AlbumId for each purchase
invoice_tracks = pd.merge(invoice_items, tracks, on='TrackId')

# Step 2: For each InvoiceId + AlbumId, count number of purchased tracks
album_track_counts = invoice_tracks.groupby(['InvoiceId', 'AlbumId'])['TrackId'].nunique().reset_index(name='PurchasedTracks')

# Step 3: Get total number of tracks per album
total_album_tracks = tracks.groupby('AlbumId')['TrackId'].nunique().reset_index(name='TotalTracks')

# Step 4: Merge to compare how many tracks were purchased vs. total tracks on album
merged = pd.merge(album_track_counts, total_album_tracks, on='AlbumId')

# Step 5: Determine if full album was purchased
merged['FullAlbum'] = merged['PurchasedTracks'] == merged['TotalTracks']

# Step 6: Join with invoice to get customer
merged = pd.merge(merged, invoices[['InvoiceId', 'CustomerId']], on='InvoiceId')

# Step 7: For each customer, determine if they have any full album purchase
customer_album_purchases = merged.groupby('CustomerId')['FullAlbum'].any().reset_index(name='BoughtFullAlbum')

# Step 8: Calculate percentage
full_album_count = customer_album_purchases['BoughtFullAlbum'].sum()
individual_count = len(customer_album_purchases) - full_album_count
total_customers = len(customer_album_purchases)

percent_full = (full_album_count / total_customers) * 100
percent_individual = (individual_count / total_customers) * 100

print("\n Album vs Individual Track Purchase Summary:\n")
print(f"Customers who bought full albums: {percent_full:.2f}%")
print(f"Customers who preferred individual tracks: {percent_individual:.2f}%")

