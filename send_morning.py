import random
import requests
import os

quotes = [
    "What are you so hesitant about? It’s your dream, isn’t it? It’s right in front of you, and you’re wavering? You gotta be reckless and take whatever you can! —Tomoya Okazaki",
    "Wake up with determination, sleep with satisfaction."
    "Rise and shine! ☀️ Every day is a fresh start.",
    "Be the energy you want to attract.",
    "The future depends on what you do today. – Gandhi",
    "If you don’t take risks, you can’t create a future. —Monkey D. Luffy",
    "Push through the pain. Giving up hurts more. —Vegeta",
    "The strong should aid and protect the weak. Then, the weak will become strong, and they in turn will aid and protect those weaker than them. That is the law of nature —Tanjiro Kamado",
    "Hard work is worthless for those that don’t believe in themselves. —Naruto Uzumak",
    "The important thing is not how long you live. It’s what you accomplish with your life. —Grovyle",
    "Nothing’s perfect, the world’s not perfect, but it’s there for us, trying the best it can. That’s what makes it so damn beautiful. —Roy Mustang",
    "Sometimes you need a little wishful thinking to keep on living —Misato Katsuragi",
    "I guess, as long as I have life, all I can do is fight with all my might. —Subaru Natsuki",
    "Sometimes, we have to look beyond what we want and do what’s best. —Piccolo",
    "All things change in a dynamic environment. Your effort to remain what you are is what limits you. —Puppet Master",
    "You're gonna care what other people think and be someone you're not your whole life? You’re fine as you are. So, talk in your own words. —Ymir",
    "You will never be able to love anybody else until you love yourself. —Lelouch Lamperouge",
    "Dead people receive more flowers than living ones because regret is stronger than gratitude. —Violet Evergarden",
    "Searching for someone to blame is such a pain. —Satoru Gojo",
    "Helping other people is the best way to make up for your mistakes —Kenshin Himura",
    "Being alone is better than being with the wrong person. — L Lawliet",
    "People’s lives don’t end when they die, it ends when they lose faith. - Itachi Uchiha",
    "A person grows up when he’s able to overcome hardships. Protection is important, but there are some things that a person must learn on his own. — Jiraiya",
    "A dropout will beat a genius through hard work. - Rock Lee",
    "Human strength lies in the ability to change yourself. — Saitama",
    "Sometimes I do feel like I’m a failure. Like there’s no hope for me. But even so, I’m not gonna give up. Ever! - Izuku Midoriya",
    "Knowledge and awareness are vague, and perhaps better called illusions. Everyone lives within their own subjective interpretation. - Itachi Uchiha",
    "You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face. — Roronoa Zoro",
    "Never trust anyone too much, remember the devil was once an angel - Kaneki",
    "Thinking you’re no-good and worthless is the worst thing you can do. - Nobito,",
    "Being weak is nothing to be ashamed of… Staying weak is!” — Fuegoleon Vermillion",
    "Fools who don’t respect the past are likely to repeat it. - Nico Robin",
    "Moving on doesn’t mean you forget about things. It just means you have to accept what’s happened and continue living. — Erza Scarlet",
    "If you feel yourself hitting up against your limit, remember for what cause you clench your fists! Remember why you started down this path, and let that memory carry you beyond your limit. - All Might",
    "A lesson without pain is meaningless. That’s because no one can gain without sacrificing something. But by enduring that pain and overcoming it, he shall obtain a powerful, unmatched heart. - Edward Elric",
    "I don’t care if no one likes me, I wasn’t created in this world to entertain everyone. - Houtarou Oreki",
    "Reject common sense to make the impossible possible. - Simon",
    "Life and death are like light and shadow. They’re both always there. But people don’t like thinking about death, so subconsciously, they always look away from it. - Yato",
    "When the world shoves you around, you just gotta stand up and shove back. It’s not like somebody’s gonna save you if you start babbling excuses. - Roronoa Zoro",
    "Power comes in response to a need, not a desire. You have to create that need. - Goku",
    "No matter how hard or impossible it is, never lose sight of your goal. - Monkey D Luffy",
    "When do you think people die? When they are shot through the heart by the bullet of a pistol? No. When they are ravaged by an incurable disease? No. When they drink a soup made from a poisonous mushroom? No! It’s when… They are forgotten. - Dr. Hiruluk",
    "Whether a fish lives in a clear stream or a water ditch, so long as it continues swimming forward, it will grow up beautifully. - Koro-Sensei",
    "Life is not a game of luck. If you wanna win, work hard. - Sora",
    "Words are like swords. If you use them the wrong way, they can turn into ugly weapons. - Edogawa Conan",
    "If happiness had a form, what would it look like? It might be something like glass, because one doesn’t notice it normally. However, it is actually there … It will state it’s presence and existence more eloquently than any other thing in this world. — Lelouch Lamperouge",
    "It's funny how each day you wake up and never really know if it will be one that will change your life forever. - Shawn",
    "There’s no shame in falling down! True shame is to not stand up again! - Shintarō Midorima"
    "Sometimes one must lose the battle in order to win the war. — Isuzu Sento",
    "Forgetting is like a wound. The wound may heal, but it has already left a scar. - Monkey D. Luffy",
    "It is at the moment of death that humanity has value. — Archer",
    "Destiny. Fate. Dreams. These unstoppable ideas are held deep in the heart of man. As long as there are people who seek freedom in this life, these things shall not vanish from the Earth. — Gold D. Rodger",
    "We can’t waste time worrying about the what if’s. - Ichigo Kurosaki",
    "There are no regrets. If one can be proud of one’s life, one should not wish for another chance. - Saber",
    "Maybe there’s only a dark road up ahead. But you still have to believe and keep going. Believe that the stars will light your path, even a little bit. Come on, let’s go on a journey! - Kaori Miyazono",
    "Those who stand at the top determine what's wrong and what's right! This very place is neutral ground! Justice will prevail, you say? But of course it will! Whoever wins this war becomes justice! - Don Quixote Doflamingo",
    "Do not think about other things, there is only one thing you can do. So master that one thing. Do not forget. What you must imagine is always that you, yourself, are the strongest. You do not need outside enemies. For you, the one you have to fight is none other than your own image. - Archer",
    "You yourself have to change first, or nothing will change for you. - Gintoki Sakata",
    "I am the hope of the universe. I am the answer to all living things that cry out for peace. I am protector of the innocent. I am the light in the darkness. I am truth. Ally to good! Nightmare to you! - Son Goku",
    "Sometimes, people are just mean. Don’t fight mean with mean. Hold your head high. — Hinata Miyake",
    "All the world’s a stage, and all the men and women merely players. - William Shakespeare" ,
    "Ask not what your country can do for you; ask what you can do for your country - John Kennedy",
    "Genius is one percent inspiration and ninety-nine percent perspiration - Thomas Edison",
    "I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character. - Martin Luther King",
    "I think therefore I am. - Rene Descartes",
    "If you want something said, ask a man; if you want something done, ask a woman. -Margaret Thatcher	",
    "I'll be back. -Terminator",
    "Keep your friends close, but your enemies closer. - Michael Corleone",
    "Knowledge is power. - Sir Francis Bacon",
    "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
    "No one can make you feel inferior without your consent. - Eleanor Roosevelt"
    "Parting is such sweet sorrow - William Shakespeare",
    "That’s one small step for a man, a giant leap for mankind. - Neil Armstrong"
    "Three can keep a secret, if two of them are dead. -Benjamin Franklin ",
    "Two roads diverged in a wood, and I, I took the one less travelled by, and that has made all the difference. -Robert Frost",
    "Whatever you are, be a good one. -Abraham Lincoln",
    "You can fool all of the people some of the time, and some of the people all of the time, but you can't fool all of the people all of the time. - Abraham Lincoln",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",

]



telegram_bot_token = os.environ.get('TELEGRAM_TOKEN')
# telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID')
chat_ids = [
    os.environ.get("TELEGRAM_CHAT_ID"),   # your own
    os.environ.get("TELEGRAM_CHAT_ID_MANU"),
    os.environ.get("TELEGRAM_CHAT_ID_YASH")
]

# print(f"Using token: {telegram_bot_token[:10]}...")
# print(f"Chat ID: {telegram_chat_id}")
# print(f"Sending quote: {quote}")


# payload = {
#     "chat_id": telegram_chat_id,
#     "text": f"🌞 Good Morning!\n\n{quote}"
# }

# response = requests.post(url, json=payload)
print(chat_ids)
for chat_id in chat_ids:
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    quote = random.choice(quotes)
    payload = {
        "chat_id": chat_id,
        "text": f"Good Morning! ✨\n\n{quote}"
    }
    response = requests.post(url, json=payload)
    print(f"Sent to {chat_id}: {response.status_code}")
# print("Status Code:", response.status_code)
# print("Response:", response.text)
