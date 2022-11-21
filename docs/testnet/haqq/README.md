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
peers="c24284f77f42a7a9d40f15e67e19bfe64320b5d3@162.55.36.64:26656,adce9d7f72360f6d66c4248b8db8de151b877130@167.235.132.152:26656,b9d04ade732a3bb91b91e279c36c6f2c12d522d3@109.107.187.78:26656,6570de868d0f7a5b4dc9f5a007ba98319a7fa8b4@194.163.162.31:26656,f2a9fa9880d31a89354250d42dd7cae5364461c7@178.20.42.155:26656,3bc11b877c2ffe5a92a33e5d2e356ba7565d733d@212.118.37.121:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,ec8a285e36888bd3134266b8ba668b48c327e6bf@142.132.202.50:36656,f4442b1ed7f64504f44ed85c89e38cfb2b19ef91@65.108.77.250:26641,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.haqqd/config/config.toml
```
