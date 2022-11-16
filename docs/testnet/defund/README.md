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

**live-peers** (31)
```
peers="c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,c0637ffa6e3a9a92c88820a8320ee58fb807706f@142.132.253.112:40656,897e47992933105fd3c466021eaa347225edc5b2@45.147.199.48:26656,921b1d0508697bbcc985900930c8da3cf5de0510@188.40.122.98:26656,14bb2fb5fb421b8036ffed04a11fe3d97ade2dbb@38.242.138.246:40656,bb25b67fd12c5b08b6d949eb21d1a3a865307e1e@95.111.243.155:40656,618eff71df45baef163034196d1cebdb9a499a39@95.217.191.74:36656,7e936b2c89d1d1a757d262bc64f981ed48fb50ec@65.21.3.229:26656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656,ac7f2212b75a01fc6c7f19ca6365a6c4b4e90cf7@88.99.122.229:26656,50ab3cea5a763fed15f18dff1f35a503f88994b2@193.203.203.27:26656,25d9dc04057628c83a3fe2406af9f1882e3ecf61@45.147.199.62:26656,d9db9bfb1e317bd16935b01a2227b699889519af@65.108.102.70:46656,760bc7fc66c15c9f2b9d722b9ee673cbdd265614@144.76.97.251:31256,fb73921dc5bf1e939308eaa37053c12bd647852b@45.147.199.210:26656,b8c444833865c545fa0b4816c6c1fd27067fc01f@161.35.16.147:56656,29ac18dffb64164b849b8ec9a29e0d3c32faa86b@62.171.183.6:26656,eaa27fa4ac25781ae7ba9a43d04f10c5890898fc@154.53.52.32:40656,3b5ae4ac36564af240b96a135eddfe856966960c@5.9.22.14:60956,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,d1d1f9b34c3e4d46d7268588848b59b3a696a533@194.233.66.70:26656,af9c5941c650bc0bfd3bacc587a05edf6603cfb1@65.108.43.113:26656,24be58ab07ed513a64b359174c6bb6a17fa112d4@65.109.17.86:41656,ded2aa043bd924c1f36151ab749b59b5749037a3@135.181.98.169:36656,2d3d11ac1f96ffb54c1df3000ed1c73684507a3b@144.91.80.32:40656,89944fe8fc90920cdd95ac8b752b81524c357961@38.242.234.75:26656,ba7d98b76435f2dad0b499429b730b817ddf85e1@45.147.199.214:26656,b3a1fda2347ffc225121793b91edd132abdcc2d9@45.147.199.63:26656,5a879e335d22f190dc614488a6a657874b66e260@62.171.162.229:36656,989c2419816cc187213cd604d09b088b4d64518c@195.3.222.189:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
