def song_decoder(song):
    list_decode = song.split('WUB')
    print(list_decode)
    list_decode_clear = [x for x in list_decode if x !='']
    print(' '.join(list_decode_clear))
    return list_decode_clear


song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND