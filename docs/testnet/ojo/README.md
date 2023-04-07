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

**live-peers** (30)
```bash
peers="ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d9df87e2e26db62ef4014ce6e8705ee11bda304f@176.124.220.21:4669,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,7ee8ece35c778418302ac085817d835b67043871@116.203.245.212:26656,899892b43b951a5bb03cb2054e4d84f6431249cc@212.227.160.56:26656,1761db35a0402af7d6008705a49dad5c9059ae63@195.231.38.226:28656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,9d6ff8ca3c73ab08b7fcd59f47ed9cf7bd80f14e@185.217.126.187:36656,da9e028814ff30ec24e94bec6887f4686f692b86@173.212.222.167:30656,59954989ec7cb0c12ec55128d142db1a274b4465@135.181.221.186:26656,d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,b16d876c443850cd358596790411b835d3f1735b@95.214.53.46:35656,98a552530acb9b0e81a834c2f514ee962da2bddf@65.109.70.45:16656,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,4640b6c775c05b6146a708a3b5ec2241c1688588@161.97.147.255:50656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,b0dac6c4a34dff86d3a77665c61bd08b4a5007cf@65.108.224.156:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
