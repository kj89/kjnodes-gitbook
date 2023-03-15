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
peers="07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,89757803f40da51678451735445ad40d5b15e059@169.155.44.106:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,9832950578c4492d934d6e875165757f5a98caff@51.83.96.150:26637,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,56bb6c5da47624a89e316ddfdd732ef78d96d79c@142.93.36.204:26656,12e6bea6650a53150c01ca3897e4a0b94d6e9d4e@135.181.141.47:26656,ae67d4c37632435e0d5f27041f50af20d227bdc2@93.170.72.118:21656,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
