def generate_insights(df):

    avg_sales_per_region = df.groupby('region')['sales'].mean()
    avg_customer_sat_per_region = df.groupby('region')['customer_satisfaction'].mean()

    print("Average Sales Per Region:\n", avg_sales_per_region)
    print("\nAverage Customer Satisfaction Per Region:\n", avg_customer_sat_per_region)

    highest_sales_region = avg_sales_per_region.idxmax()
    lowest_sales_region = avg_sales_per_region.idxmin()

    lowest_satisfaction_region = avg_customer_sat_per_region.idxmin()
    highest_satisfaction_region = avg_customer_sat_per_region.idxmax()

    print("\n" + "=" * 50)
    print("INSIGHTS")
    print("=" * 50)

    print("\nInsight 1:")
    print("----------------------------------------")

    #highest sales and lowest satisfaction
    if(highest_sales_region == lowest_satisfaction_region):
        print(f"Observation:\nThe {highest_sales_region} region has the highest sales but the lowest customer satisfaction.")
    else:
        print(f"Observation:\nThe {highest_sales_region} region has the highest sales, while the {lowest_satisfaction_region} region has the lowest customer satisfaction.")

    print(f"Recommendation:\nInvestigate customer experience in the {highest_sales_region} region.")
    
    print("\nInsight 2:")
    print("----------------------------------------")
    #lowest sales and highest satisfaction
    if(lowest_sales_region == highest_satisfaction_region):
        print(f"Observation:\nThe {lowest_sales_region} region has the highest customer satisfaction but relatively low sales.")
    else:
        print(f"Observation:\nThe {highest_satisfaction_region} region has the highest customer satisfaction, while the {lowest_sales_region} region has the lowest sales.")

    print(f"Recommendation:\nIncrease marketing or sales efforts in the {lowest_sales_region} region and consider applying successful strategies from the {highest_satisfaction_region} region.")