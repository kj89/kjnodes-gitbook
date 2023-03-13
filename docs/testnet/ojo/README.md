# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)




## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: [https://ojo-testnet.grpc.kjnodes.com](https://ojo-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:50656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:50659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (40)
```bash
peers="3de750927e66b01bb566c1c189beeb43b7cde73f@213.239.216.252:47656,67a1f07c7743d9bec92e11faad5bffe9bc08a178@130.185.119.243:50656,affee2f485ca15c68c302ad98e8de41fcd0e71ba@162.19.238.49:26656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,cd4d7ffdad8bd258cd90c22ec7197c0fdf9f3648@38.242.134.73:27656,cabd6a59d90f477a4dd04e87543d01f97b9b619e@185.9.144.138:46656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,3de7e03a2c6c50e5c38309d47ecfbf14ddf5304e@65.109.115.237:50656,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,dd55e293588003da8cd6cf56a0e6c6cdab1f6e75@176.37.119.156:26694,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,dacdb802de389deb5ccf9100e049209f55f62854@188.40.98.169:29656,3d11a6c7a5d4b3c5752be0c252c557ed4acc2c30@167.235.57.142:36656,b16d876c443850cd358596790411b835d3f1735b@95.214.53.46:35656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,e7689e281278e2e52c95962cab219e681b641c1a@46.0.203.78:21656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,8ee9b08d75823b13ca5517c3469f6aaf541aa684@65.108.43.58:27675,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,d69bb338dcc2aa6a00961731b4ca6746132ef356@1.162.83.160:26656,97ff540b57b89dd0b6737eddb92977523dd5a7b3@195.3.221.58:12656,948d955c744ef88481807d0209c2ab76677d6bc7@80.70.105.73:27656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,93003c656ea73cf54164274f271dc5ccd1d493be@178.124.214.192:32656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
