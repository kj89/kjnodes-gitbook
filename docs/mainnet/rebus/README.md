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
peers="6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,afdd27b58e851dcbb8c98c0e3191a0d8bfbcd3ae@65.108.41.252:26656,1749a8f0aa533fc92c1212366c22c0993fbb1545@51.178.47.116:26656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
