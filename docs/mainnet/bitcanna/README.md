# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)


## Public endpoints

* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```bash
peers="07c829cf936db34be61143fabb09541d05aea899@65.108.98.124:64206,8a210f1bcfc9015a7bc18dcc5add29c0dce3f2dc@135.181.173.65:26656,da04ee3f8bd93421a3264e3a061a09c139aaa937@161.97.150.65:26656,0a658df9d9fab096983a12e6f878e87281a15ce6@194.163.172.37:27656,45589e6147e36dda9e429668484d7614fb25b142@135.181.139.113:27656,90ee680b1738344354c48c23ba1e1fd68e071d80@142.132.248.138:26696,d8a0facda705edbbdd2d79fb302e017df009e9da@207.244.231.189:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,4e1c2471efb89239fb04a4b75f9f87177fd91d00@95.217.151.241:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
