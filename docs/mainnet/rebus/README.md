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

**live-peers** (30)
```bash
peers="275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,ea5e7a6b9a5c18c6455e7a8c583c129c5821a452@51.178.80.111:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,05483a7ec0160b17de1ad8e7793c7502e70e5525@146.59.85.223:17256,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
