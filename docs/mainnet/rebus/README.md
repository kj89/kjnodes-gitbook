# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: rebus.grpc.kjnodes.com:21090

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

**live-peers** (20)
```bash
peers="346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,d12f9b52ca0e11cdeca5c46e802249ade4c39c45@185.248.24.40:26656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,275d2614d24c8ac015a7712702fcb99cef67ef67@65.108.124.219:29656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
