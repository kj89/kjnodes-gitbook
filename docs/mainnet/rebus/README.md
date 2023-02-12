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
peers="07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.207:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,241c83e7a6ff769d66be0c4848db44cdcac8b4b0@192.99.62.83:26656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,6dc49b312a98051351f0347568c294fea83a5f9a@51.79.27.21:11656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656,09e5d302fd49709b5b46d391a297f448a5dc1a37@65.109.82.249:30656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
