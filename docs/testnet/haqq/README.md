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
peers="0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,6aceb34e71a634437bb848fdf9299bc8b07fa303@95.217.224.229:26656,88f134e7caad68e01554f4d648069c443a21fd4c@135.181.35.46:36656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656,99a8389c84625503c2b8d734dfd78035d28e4f15@65.109.30.117:26656,0760b7526738dac0af14b5e3d3b62e49c63dd490@185.154.14.142:26656,26a5bd6fb59f4dcd25f20bbc53b88860b2598f7d@65.21.91.50:35656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
