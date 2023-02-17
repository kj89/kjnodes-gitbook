# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-2 | **Latest Version Tag**: v0.16.3 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (32)
```bash
peers="62f26443c930a02f3e166b9db4ecd37b65b042f2@49.12.8.255:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,39429c00e9d451a5a449deec38067bea37a8e43c@164.92.122.128:26656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,09c05898d64d2ec387e27ae3e1029a2f53a2a1dc@155.133.22.109:26656,2e2a71b2fc86986a7940df724ce100c45cca3649@66.94.104.184:26657,d2b6baed49aa475eb6ec5958bfbca30a61363b86@154.53.52.212:26657,b57a9c1e7c0f597c9ef6a47cc361094f95a22b84@192.9.134.157:27656,09de7d3f5acc5e421247a582aa50d601571415fb@38.242.202.200:26656,a94ef19317c0b592cc3d6ac10501d0f4fc099d47@85.173.113.198:21656,14400308576815f96bdec78848a570e07c14f412@91.195.101.99:26656,d40bd2a7a5d3dc525e66be78a2bdaf1ff0bc1957@95.214.55.25:29656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,162ab520aaacad1d62e3d051246f5fe1ba9dc9c6@65.109.17.23:56112,7f30e0e50fa219fad61b1378592285f6ee2b70dc@144.76.90.130:36656,24016cec78971d7ecae24fd99ac16655e6332eb8@66.94.102.176:26657,3030536f218c76eb43d05035ac64dda277cdc14d@109.172.45.7:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,d212c993e5b503cf224592bf426d3fb808d84e98@5.161.48.209:26656,50f70faf399aac827000458d49cdf4ea18f4fb82@95.217.163.250:26656,719e5c2c79f027c65514d70e0f08d754119a6f0c@45.10.154.246:26656,438701ce016699880f9073c6b99f71d17309d820@154.53.52.215:26657,f978d2dde4b300037c7d2bccb47af9998045bc68@146.0.41.65:39656,3997242f9646ca642932852b7577ddb9976e0396@5.199.130.53:26656,7e465cf7525009fa55c8387eb74a330d3b96e26f@86.48.5.78:26656,5a868d18a5046b715ee726a45b680a68f92bafcb@149.102.136.149:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
