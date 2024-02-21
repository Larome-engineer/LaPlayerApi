from laplayer_api.data.variables import word_list


# filename = re.sub("[^A-Za-zА-Яа-я0-9–&ÄäÖöËëẞßÜüЁёЇїІіҐґЄ,є$(+)/|.~']", ' ', f"{yt.title}").strip()


def filter_name(yt):
    try:
        filename = yt.title.replace('—', '-').replace('*', '^').replace('|', '#').replace('?', '.').replace("/", "'")
        if '-' in filename:
            author = filename.split(' -')[0]
            name = filename.split('- ')[1]
        else:
            name = filename
            author = yt.author

        start_bracket_index = name.find("(")
        end_bracket_index = name.find(")")

        if start_bracket_index != -1 or end_bracket_index != -1:
            into_brackets = name[start_bracket_index + 1:end_bracket_index]

            for word in into_brackets.split(' '):
                if word.lower() in word_list:
                    name = name.split('(')[0].strip()
                    break

        if author == '':
            author = yt.author.strip()
        else:
            author = author.strip()

        print(f'--FILENAME:{filename}')
        print(f'--AUTHOR:{author}')
        print(f'--NAME:{name}')

        return author, name
    except IndexError:
        return None
