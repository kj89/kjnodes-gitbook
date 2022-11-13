# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

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

**live-peers** (15)
```
peers="e2542af1f83025786c34947f1b6d39a511500327@173.249.20.104:26656,83902507559b71918fbeeb54ccb31411917c219d@135.181.25.153:26656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,ac7f2212b75a01fc6c7f19ca6365a6c4b4e90cf7@88.99.122.229:26656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,897e47992933105fd3c466021eaa347225edc5b2@45.147.199.48:26656,156eb5692a8ea7252ea58fecf82781fc23a6f29e@109.123.246.107:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656,29ac18dffb64164b849b8ec9a29e0d3c32faa86b@62.171.183.6:26656,b5252eac7b8bc4d5d2cc211bc794f8b4e62d2cc4@188.34.154.116:26656,8190bf19ef96627e3b35f2039ab6aeed551fa05c@167.235.201.57:26656,8ac1ab46e98ebd14b7493dbf83c1e33cd2aa5921@45.87.154.227:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
