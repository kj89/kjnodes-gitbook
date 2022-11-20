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

**live-peers** (29)
```
peers="fe32ed5f0a7f8928f8299d8dd78fc5b650472ac4@65.108.46.123:56656,897e47992933105fd3c466021eaa347225edc5b2@45.147.199.48:26656,75e38d35a430a9c1ac65249db3d4cab245159a8b@144.91.97.124:26656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@168.119.227.28:36656,50ab3cea5a763fed15f18dff1f35a503f88994b2@193.203.203.27:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,d04084623a4ec44fd91d46f07ba2e2d1d0638dd4@141.95.23.183:26656,9ae365f1c4a2b95c95fdcaa92db4a4f5a655ef1f@5.161.108.72:26656,409d5422d6934b0dedfd3347e078b67aac691120@45.147.199.185:26656,2d67fa34c0ecf8742f3efa7823271569dbe635b9@91.194.11.245:26656,328a8e2173b0fd3083829e6e0fd55cbc5d51083d@217.13.223.167:26656,606f26956b8387de65010b6fe74cc06b5989c5de@178.63.8.245:60656,3441bf28387afc7d9b6e7a754c3ed37f21006859@5.161.134.231:26656,2b14bde73df424ddc56fe940ff546e6c88c8e5fa@185.63.191.143:26656,921b1d0508697bbcc985900930c8da3cf5de0510@188.40.122.98:26656,bad21eb0dd7d2002912acc42a89b66a0deb44a03@65.21.134.202:26576,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,7831e762e13c2cb99236b59f5513bf1f8d16d036@88.99.3.158:10356,c7d10d48cd7723f1ed661d20baa3ffba3e7a8b80@104.193.254.108:40656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,29ac18dffb64164b849b8ec9a29e0d3c32faa86b@62.171.183.6:26656,2c4ddd8d4af5405618098648864d1d9975024aa3@95.216.173.157:26656,ad6dbf9a584643cb986b81a06efe425623e48df6@65.109.84.215:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,83902507559b71918fbeeb54ccb31411917c219d@135.181.25.153:26656,ef4cac7e5813a753239239e297efcabc03a07fbb@194.180.176.125:26656,fdb34ea011301410cf6231307287df27befe7049@85.114.142.242:46656,25d9dc04057628c83a3fe2406af9f1882e3ecf61@45.147.199.62:26656,156eb5692a8ea7252ea58fecf82781fc23a6f29e@109.123.246.107:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
