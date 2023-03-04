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

**live-peers** (19)
```bash
peers="92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,d3a8fdbe6776fc71998fa893abcd634461b52b19@65.109.92.241:40106,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,4e3e545e85000045ef44905ab683a5db6f87cdbe@88.198.32.17:37656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
