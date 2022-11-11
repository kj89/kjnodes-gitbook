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

**live-peers** (34)
```
peers="f114c02efc5aa7ee3ee6733d806a1fae2fbfb66b@65.109.49.111:21656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656,d9db9bfb1e317bd16935b01a2227b699889519af@65.108.102.70:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,5f27d363c126cf7f7e1e9cab2dadd62862109e3d@65.21.227.112:26656,88a50213aa1c3767d4014dbebd18bff8853d43c6@161.97.73.21:26656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,ec80e423e75ae61ecd24bf29f0a9b0720070e074@78.46.106.75:26656,bef3701487b54ba73de5e0d84ac57fc2a54f3a5f@45.147.199.67:26656,24be58ab07ed513a64b359174c6bb6a17fa112d4@65.109.17.86:41656,897e47992933105fd3c466021eaa347225edc5b2@45.147.199.48:26656,6cefbf7a3c4435b19ecf24fc8cc982f7c1353eb7@65.21.58.131:36656,b50363075f36fa3382f78bdbe0c297dd27465eeb@154.38.161.212:26656,5eb5ce58df3b4dfaf3f04d48a54789a0b4b1007a@154.12.239.248:26656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,25d9dc04057628c83a3fe2406af9f1882e3ecf61@45.147.199.62:26656,028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,f282bfeabf20962bc26bad0bdec53d6729828faf@45.147.199.203:26656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,156eb5692a8ea7252ea58fecf82781fc23a6f29e@109.123.246.107:26656,618eff71df45baef163034196d1cebdb9a499a39@95.217.191.74:36656,0c0772f5c52a95412208acfa579ef5adb4266ec1@92.38.241.107:26656,5a1977f1db820b7ee4719abbbff6f721f14176eb@65.109.84.254:36656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,1620f27c3d9f84fb0b48a179f51d92831ee72b58@88.99.84.177:26656,888c32ea9a3448de1f5f7d014a42c7437bd75aa3@65.21.121.101:36656,b3a1fda2347ffc225121793b91edd132abdcc2d9@45.147.199.63:26656,4d2f9132892d172b79cf00937fd554bd0f6a263c@92.119.112.200:26656,921b1d0508697bbcc985900930c8da3cf5de0510@188.40.122.98:26656,84c120f1b65467320292ff0a88f453f24079196e@65.109.82.75:36656,b32e6619a1c7998519d2d38828e34ace7b773852@65.109.84.250:36656,409d5422d6934b0dedfd3347e078b67aac691120@45.147.199.185:26656,5a879e335d22f190dc614488a6a657874b66e260@62.171.162.229:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
