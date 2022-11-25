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
peers="a8b07f98f5fcacb358e063d33eeb1d5953e90650@65.108.11.180:33656,24da98830276fb0b4fc209cfcaf0cc3a287e1bdd@135.181.222.179:26656,f4442b1ed7f64504f44ed85c89e38cfb2b19ef91@65.108.77.250:26641,562a589b82682f695344bc4a9d7a2fcb5a5a4d80@65.21.60.82:26656,88f134e7caad68e01554f4d648069c443a21fd4c@135.181.35.46:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,849d98423e3f757233bef91d7b80937329d7684f@162.19.131.173:26656,001eb7a3a03dc11539541737262c4ddc84dec283@91.195.101.98:26656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
