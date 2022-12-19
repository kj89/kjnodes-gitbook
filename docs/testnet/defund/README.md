# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (12)
```
peers="a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,b3ea7a581e2f1c1e19d2067e6cd54497914ec4ea@173.249.54.237:40656,6bbd4d421c9610e918fee90a81278e689e445d81@194.163.184.53:40656,028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,a7cf78c4ec7bf69731c2cc9a5c1064e71e8e27d1@38.242.251.116:26656,f02544ad936678f3c6f23897daee2c807b3d293c@45.147.199.188:26656,9e3c8603f8eb1aeacf7392701a1977668684803c@194.163.170.245:26656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,b712dfb6043ada3c0b981a4a5ec6b5f7658cc4d8@173.249.51.180:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,ad35b87df11c37b5f66931cd86c5dc2853aabae2@95.216.69.88:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
