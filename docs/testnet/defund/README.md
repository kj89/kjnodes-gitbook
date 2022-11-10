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

**live-peers** (25)
```
peers="ec80e423e75ae61ecd24bf29f0a9b0720070e074@78.46.106.75:26656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@168.119.227.28:36656,0a006400acd379fc12ac36bfaab859777b1f0b33@62.212.65.138:23656,29ac18dffb64164b849b8ec9a29e0d3c32faa86b@62.171.183.6:26656,d9db9bfb1e317bd16935b01a2227b699889519af@65.108.102.70:46656,af9c5941c650bc0bfd3bacc587a05edf6603cfb1@65.108.43.113:26656,f114c02efc5aa7ee3ee6733d806a1fae2fbfb66b@65.109.49.111:21656,5eb5ce58df3b4dfaf3f04d48a54789a0b4b1007a@154.12.239.248:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,b8c444833865c545fa0b4816c6c1fd27067fc01f@161.35.16.147:56656,cd53ab15aa53f7fd0f584bb60b253a4d53246867@93.189.30.116:26656,fd40c978275ceb1e0f9a81a7f40b3ec5f8b7b544@195.201.237.184:36656,28f14b89d10992cff60cbe98d4cd1cf84b1d2c60@88.99.214.188:26656,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,88a50213aa1c3767d4014dbebd18bff8853d43c6@161.97.73.21:26656,ef4cac7e5813a753239239e297efcabc03a07fbb@194.180.176.125:26656,8ac1ab46e98ebd14b7493dbf83c1e33cd2aa5921@45.87.154.227:26656,2d67fa34c0ecf8742f3efa7823271569dbe635b9@91.194.11.245:26656,eaa27fa4ac25781ae7ba9a43d04f10c5890898fc@154.53.52.32:40656,868bee888f452324c01b6c3b67ef8b6082e57025@195.201.164.125:29656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,d1d1f9b34c3e4d46d7268588848b59b3a696a533@194.233.66.70:26656,b50363075f36fa3382f78bdbe0c297dd27465eeb@154.38.161.212:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
