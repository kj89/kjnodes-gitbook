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
peers="b4c7205397045d22fe762c8d2021fa4ce6d7ea1e@162.55.39.159:36656,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,d013ef148dd0eef23d338658ecf857682934296a@65.109.61.100:50656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,7afbf90f6ea9639c783ed38a2628a402bf3d912b@109.205.180.81:56656,eda9eb97425808e8261c8c05fb31892ac26dd458@185.246.86.50:26656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,1e2a49792b0e0686827ec0fbc101a9ad709e0f28@88.210.9.78:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,8b6c75d20ac3ceeb7f0f1d4b5fc89a69e567c47b@65.108.231.238:36656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,5af793eef9fcf435520cfb8674b3339f5f03c340@104.248.45.68:24656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,cd4d7ffdad8bd258cd90c22ec7197c0fdf9f3648@38.242.134.73:27656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,62fa77951a7c8f323c0499fff716cd86932d8996@65.108.199.36:24214,ea0ad608f0fa47e20047569c7c0c1ff76dd3d724@45.151.123.72:28656,969b1e53d217abf769054777190f9a65eb8174cf@46.4.61.91:26656,2691bb6b296b951400d871c8d0bd94a3a1cdbd52@65.109.93.152:33656,944b6c69c4abec63a06016238799b3846d47f8e6@65.109.116.119:50656,da9e028814ff30ec24e94bec6887f4686f692b86@173.212.222.167:30656,8e2ea63e2ff7ecbe75aef6012c4df050d5e1de0f@65.21.139.155:28656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:26656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
