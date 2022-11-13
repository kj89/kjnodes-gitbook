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

**live-peers** (28)
```
peers="77a7c437c7e0c421eeaebe677235306d2466da4c@91.194.11.156:26656,bad21eb0dd7d2002912acc42a89b66a0deb44a03@65.21.134.202:26576,324c36dcc39039d6c8007711b5923b4645c93202@142.132.202.50:46656,d9db9bfb1e317bd16935b01a2227b699889519af@65.108.102.70:46656,9e1c29e75bf7dabdd43a27898148195d198a9aa0@188.34.178.184:18656,01a4dbeb9cdb8fc7086199a7111381735f4c5f41@176.9.106.43:26656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,f282bfeabf20962bc26bad0bdec53d6729828faf@45.147.199.203:26656,6831595408fec957b580907a36b179d8d5aa37c0@94.130.225.41:26656,025cb244b9a4d30362d4aed4a4c60ff7c3ff5d71@142.132.232.175:26656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,156eb5692a8ea7252ea58fecf82781fc23a6f29e@109.123.246.107:26656,83902507559b71918fbeeb54ccb31411917c219d@135.181.25.153:26656,b8c444833865c545fa0b4816c6c1fd27067fc01f@161.35.16.147:56656,f657421825c924c583994fa0e4543b613519ca50@45.147.199.6:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,bef3701487b54ba73de5e0d84ac57fc2a54f3a5f@45.147.199.67:26656,8ac1ab46e98ebd14b7493dbf83c1e33cd2aa5921@45.87.154.227:26656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,90dc33a14889c0a0348b18a03d2a3d0eab41e6cb@92.119.112.225:26656,114d6ed1ee640298baa1a695367e9e9189078154@92.119.112.231:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,c0637ffa6e3a9a92c88820a8320ee58fb807706f@142.132.253.112:40656,5a879e335d22f190dc614488a6a657874b66e260@62.171.162.229:36656,d1d1f9b34c3e4d46d7268588848b59b3a696a533@194.233.66.70:26656,4d2f9132892d172b79cf00937fd554bd0f6a263c@92.119.112.200:26656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656,989c2419816cc187213cd604d09b088b4d64518c@195.3.222.189:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
