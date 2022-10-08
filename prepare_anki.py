# https://github.com/kerrickstaley/genanki
import genanki
from os import listdir
from os.path import isfile, join

my_model = genanki.Model(
  1234567534,
  'Simple Model with Media',
  fields=[
    {'name': 'Picture'},
    {'name': 'Answer'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Picture}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_deck = genanki.Deck(
  3234561213,
  'Geoguessr Bollards')

folder = 'bollards'
files = [f"{folder}/{f}" for f in listdir(folder) if isfile(join(folder, f))]
media_files = []
for f in files:
    file_name = f.split('/')[-1]
    country_name = file_name.split('_')[0]
    if country_name != '':
        media_files.append(f)

        my_note = genanki.Note(
            model=my_model,
            fields=[f'<img src="{file_name}">',country_name])

        my_deck.add_note(my_note)

my_package = genanki.Package(my_deck)
my_package.media_files = media_files
my_package.write_to_file('bollards_anki_deck.apkg')