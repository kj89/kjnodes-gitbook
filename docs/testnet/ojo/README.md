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

**live-peers** (41)
```bash
peers="91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,7afbf90f6ea9639c783ed38a2628a402bf3d912b@109.205.180.81:56656,cd4d7ffdad8bd258cd90c22ec7197c0fdf9f3648@38.242.134.73:27656,e052b7c899bae41f6d89f70f81de50e28b72a7bf@38.242.237.100:26656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,4e007fe2793172797eff893abf91ab685549ee11@65.109.235.2:26656,f70138a8bbca35814ed947184821f8a561651793@185.234.69.143:30656,06c7ca04fb5965096396b78ff8af7f2c408382bc@38.242.133.8:26656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656,3aeec94e9567c66ad6bb76b496aff6d55fd53d32@65.109.171.22:26656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,3130147135ce803784e0941aecbcc2597bc74425@85.214.116.96:33656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,36ebf858ef7dd3b96790eb3f9c7a9b14282f8afe@135.181.16.252:27656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:26656,58f192f7c6aebe881f54bd133e9b8abf82bc3b20@65.108.13.154:36656,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,591f458674336b90f06e4669bcf459084f34d191@167.235.139.171:26656,b2291ae6c53a078f414f5652b37ecf59b6eabb09@91.107.237.224:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
