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

**live-peers** (18)
```bash
peers="e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,5fb9952f3eaeb5be3aab37425831c2a4830a019d@65.21.133.125:29656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
