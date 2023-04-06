import pandas as px

# reads csv file
df = px.read_csv("hotels.csv", dtype={"id": str})


# prints the hotel list
def print_df():
    print(df)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"

        # Edits the available column without adding a new column
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Spa(Hotel):
    def book_spapackage(self):
        pass

if __name__ == "__main__":
    print_df()