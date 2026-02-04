# Hotel Booking Analysis: Metric Definitions & KPI Framework

## 1. Overview
This dictionary defines the Key Performance Indicators (KPIs) used in the Hotel Booking module of the Business Intelligence Portfolio. Standardizing these definitions ensures consistency across SQL queries, Python analysis, and Tableau/Power BI visualizations.

## 2. Revenue Metrics

### ADR (Average Daily Rate)
- **Definition:** The average rental income per paid occupied room in a given time period.
- **Formula:** `Total Room Revenue / Number of Rooms Sold`
- **Business Impact:** Primary indicator of pricing power and market positioning.

### RevPAR (Revenue Per Available Room)
- **Definition:** Total room revenue divided by the total number of available rooms (including those not sold).
- **Formula:** `Total Room Revenue / Total Rooms Available` OR `ADR * Occupancy Rate`
- **Business Impact:** The "Holy Grail" of hotel metrics. It measures the hotel's ability to fill rooms at an average rate.

## 3. Operational Metrics

### Occupancy Rate
- **Definition:** The percentage of available rooms that were sold.
- **Formula:** `(Total Rooms Sold / Total Rooms Available) * 100`
- **Context:** High occupancy with low ADR suggests underpricing. Low occupancy with high ADR suggests overpricing.

### Cancellation Rate
- **Definition:** The percentage of bookings that are cancelled before check-in.
- **Formula:** `(Total Cancelled Bookings / Total Bookings) * 100`
- **Insights:** High cancellation rates on specific channels (e.g., OTA vs Direct) may indicate pricing disparities or poor user qualification.

### ALOS (Average Length of Stay)
- **Definition:** The average number of days guests stay in the hotel.
- **Formula:** `Total Room Nights / Total Bookings`
- **Strategy:** Increasing ALOS reduces turnover costs (cleaning, check-in processing).

## 4. Customer Segmentation Dimensions

- **Lead Time:** Days between booking date and arrival date. (Short vs. Long window planning).
- **Market Segment:**
    - *Transient:* Individual travelers (Higher ADR, less predictable).
    - *Corporate:* Business contracts (Lower ADR, high volume/predictability).
    - *Groups:* Large blocks (Lowest ADR, fills base occupancy).
