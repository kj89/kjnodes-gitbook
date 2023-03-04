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

**live-peers** (18)
```bash
peers="5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,e6f1684ed8ed5c586b188bf7088026da4ffdaff6@134.65.193.78:26656,87102b5dd22c1d17f97197c078f23726ae3c6214@91.157.60.253:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
