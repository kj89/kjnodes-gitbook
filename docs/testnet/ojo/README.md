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

**live-peers** (34)
```bash
peers="ac5089a8789736e2bc3eee0bf79ca04e22202bef@162.55.80.116:29656,cd4d7ffdad8bd258cd90c22ec7197c0fdf9f3648@38.242.134.73:27656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,e6b70cf272ec33d3915a94c60b68637935643fd3@194.163.167.138:59656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,affee2f485ca15c68c302ad98e8de41fcd0e71ba@162.19.238.49:26656,d9df87e2e26db62ef4014ce6e8705ee11bda304f@176.124.220.21:4669,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:26656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,2a4497089e7076c2d836741ae38a64138233bb4b@165.22.60.23:26656,969b1e53d217abf769054777190f9a65eb8174cf@46.4.61.91:26656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,0ccc4bd8386fbec1421e3c19c24124eeb00b3293@46.101.144.90:28656,952f01b8486a99436a5ade5a0c20089838b0427f@31.220.90.158:26656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
