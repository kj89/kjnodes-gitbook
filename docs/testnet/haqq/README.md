# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.2.1 | **Wasm**: OFF

Website: [https://islamiccoin.net](https://islamiccoin.net)


## Public endpoints

* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```
peers="9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,001eb7a3a03dc11539541737262c4ddc84dec283@91.195.101.98:26656,fd53be6145264c86f2db22659141c925e119794c@138.201.155.226:12656,0ba87cb7b55b15e6b33b6703dc681c84332273e5@168.119.165.65:12656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,35e1bf6fda8a37c9c4872527a30b1fe26b0a155f@45.13.59.201:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,1b9b907b4bf609c7acf47a20bd23320c9e73b784@135.181.222.185:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
