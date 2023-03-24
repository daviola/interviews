# -*- coding: utf-8 -*-

def update_dexterity_and_elixir(item):
    if item.quality > 0:
        item.quality = item.quality - 1
    item.sell_in = item.sell_in - 1
    if item.quality > 0 and item.sell_in < 0:
        item.quality = item.quality - 1

def update_backstage(item):
    if item.quality < 50:
        item.quality = item.quality + 1
    if item.sell_in < 11:
        if item.quality < 50:
            item.quality = item.quality + 1
    if item.sell_in < 6:
        if item.quality < 50:
            item.quality = item.quality + 1
    item.sell_in = item.sell_in - 1

def update_mana_cake(item):
    if item.quality > 0:
        item.quality = item.quality -2
    if item.quality > 0 and item.sell_in < 0:
        item.quality = item.quality - 2
    item.sell_in = item.sell_in - 1

def update_aged_brie(item):
    if item.quality < 50:
        item.quality = item.quality + 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0 and item.quality < 50:
        item.quality = item.quality + 1


class GildedRose(object):

    categories = {
        "+5 Dexterity Vest": update_dexterity_and_elixir,
        "Elixir of the Mongoose": update_dexterity_and_elixir,
        "Backstage passes to a TAFKAL80ETC concert": update_backstage,
        "Conjured Mana Cake": update_mana_cake,
        "Aged Brie": update_aged_brie,
    }
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        [self.categories[item.name](item) for item in self.items if item.name in self.categories]        

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
