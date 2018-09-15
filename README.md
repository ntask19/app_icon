# スマホアプリのアイコンリサイズ

スマホアプリ作成で不可欠な各サイズのアイコンをリサイズできるスクリプトです。

## 必要なもの

- iOSストア用アイコン（1024×1024）
- Androidストア用アイコン（512×512）
- Android用ステータスバーアイコン（144×144）

※ 全て揃ってなくても使えます。

## 実行環境

- Python3
- Pillow

## 使い方

準備したアイコンをinputに入れます。

```
python3 icon.py
```

を実行します。後は、outputに画像が書き出されているので、アプリに組み込むことが出来ます。


## おまけ

生成する画像名とサイズは `icons.json` で設定しているので足りない・いらない画像があればjsonをいじるだけでOKです。