# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (20)
```bash
peers="d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,49e084a4c77f168810608e20b530ee9d25ac69b7@209.126.8.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
