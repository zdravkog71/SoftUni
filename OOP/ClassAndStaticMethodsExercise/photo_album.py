import math

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []


    @property
    def photos(self):
       return self.__photos

    @photos.setter
    def photos(self, value):
        for _ in range(self.pages):
            value.append([])
        self.__photos = value



    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        if len(self.photos[-1]) == 4:
            return f"No more free slots"

        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"


    def display(self):
        dashes = "-" * 11
        result = f"{dashes}\n"

        for pages in (self.photos):
            row = ""
            for _ in pages:
                row += "[] "
            row = row.strip()
            result += row + "\n"
            result += f"{dashes}\n"
        #result +=
        return result.strip()



# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# print(album.display())


# AssertionError: Lists differ: [] != [[], []]
#
# Second list contains 2 additional elements.
# First extra element 0:
# []
#
# - []
# + [[], []]

# album = PhotoAlbum(3)
# for _ in range(8):
#     album.add_photo("asdf")
# result = album.display().strip()
# print(result)


import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()