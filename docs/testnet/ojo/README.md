# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:50090

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

**live-peers** (42)
```bash
peers="4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,6cbb393c7b4b061a3b63d8061e67ce8fcf53f8d6@95.214.55.109:2626,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,c2ed1269cd275202e4d69fdb64e194e59b20f573@185.245.182.152:40656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,7bf4e4a18bf2006f79f50c79903f77d4e2a5a303@65.21.77.175:33307,bdd24cab3246503ae261aea82f077ffb66d56ce3@95.216.39.183:28656,d6b0791afd2d41c47bce8c152174b40c230988ba@138.201.225.104:47756,5ca82e3383c750de5a7d47a084c9a67fef0847dd@159.89.21.115:26656,2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,d9df87e2e26db62ef4014ce6e8705ee11bda304f@176.124.220.21:4669,5af3d50dcc231884f3d3da3e3caecb0deef1dc5b@142.132.134.112:25356,d30444b8fc8ae5867cd620651fdef2a064fded2a@89.64.74.222:26656,1786d7d18b39d5824cae23e8085c87883ed661e6@65.109.147.57:36656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,9dc1f555bd37d6840237f32a2cd4d79ba1c80cb5@65.108.227.112:31656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,18300f0a5973798c3900fe51ff255bb6bca982f9@65.109.65.248:36656,4640b6c775c05b6146a708a3b5ec2241c1688588@161.97.147.255:50656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,0ea23938eaefffe447eb0126d4951e2ac9c45637@45.140.147.252:26656,057e1ebe8aed2c27bcacb0eeb54dee01f3c6eddd@65.108.200.49:8656,ae3b71414e67664f0eafa115980ad0e5c2aa9985@176.37.119.156:26694,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,4c66c9cd1bd73a2e8ff7fde84292850f9002efdc@65.109.92.148:26656,d0973fcf352a68fda91624f05b7d90e171cce032@65.109.28.226:05656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
