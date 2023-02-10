# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: [https://rebus.grpc.kjnodes.com](https://rebus.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```bash
peers="fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
