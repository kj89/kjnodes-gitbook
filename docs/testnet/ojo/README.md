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

**live-peers** (38)
```bash
peers="ffe2d5ecb614762d5a1723f5f8b00d3feb6eb091@5.9.13.234:26686,c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,da9e028814ff30ec24e94bec6887f4686f692b86@173.212.222.167:30656,17a5fad48064ee3da42f435925f7bbe055e6348d@65.108.233.102:37656,f6d6e625759814e157457a5889961e02dba26ba6@65.109.92.240:37096,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,2a4497089e7076c2d836741ae38a64138233bb4b@165.22.60.23:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,978cf9aca38f819fd8189272379fc3c2ae2682a8@213.239.218.210:56656,58f192f7c6aebe881f54bd133e9b8abf82bc3b20@65.108.13.154:36656,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,944b6c69c4abec63a06016238799b3846d47f8e6@65.109.116.119:50656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,57847cb629cd707515b838a5baaf2b5c3ca0b022@65.108.199.206:37656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,2086389fe8bb43133205d1a76792b5e58bc9f811@65.108.197.164:64646,1e2a49792b0e0686827ec0fbc101a9ad709e0f28@88.210.9.78:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:40256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
