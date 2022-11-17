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
peers="0c0e74c0550f5c394537f81617a6fd8480381654@94.130.142.27:36656,24cee16ef3d1fa790a4f07212974047369a3e969@198.204.255.156:26656,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,d648d598c34e0e58ec759aa399fe4534021e8401@109.205.180.81:26656,5c11c697aaf2dabf96e3eb7e7e621c200bd309ee@65.21.225.58:26656,0d600b8281ee6a710c213023755d2382cf90af13@116.202.165.116:46656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,adce9d7f72360f6d66c4248b8db8de151b877130@167.235.132.152:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
