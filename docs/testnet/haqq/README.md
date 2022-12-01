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
peers="181c3ef9dba190c45ad8143550188d24e471b7a5@148.251.47.69:16656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,4034efbff7c82e1a2d3908fefd2512552dea63f5@65.109.38.208:26651,0409afd9db164813d8e5f29eb9e0d5edbd3c7ba0@5.189.163.114:26656,e3f0c86ff89c50e96833c70114beeb04ac9c803f@178.18.251.118:26656,88b8b733d8b96e9a518c1a8bea4dbc5bf896026e@5.161.156.183:26656,88f134e7caad68e01554f4d648069c443a21fd4c@135.181.35.46:36656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
