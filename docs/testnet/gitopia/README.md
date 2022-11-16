# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (22)
```
peers="db5f2aeda7308f395b7e32a65aec7b8b23a6817f@95.216.161.242:19656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,8a86d39f08c47ed0ef2bd21606f16817744a3742@38.242.203.117:26656,61f824be9bdfe9a73b55ad162a9ed0bfe9121bbe@38.242.147.76:26656,32d6752d6077286da2bda0a79278606432e69144@65.109.84.214:60956,a5369601c7a7e44a5fdc893540d706c87a48a58c@185.197.251.195:41656,eec3daeed105dcd5647d1fc24ef8f1d0f404f2fe@167.235.21.149:29656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,afbed8b52881b2f783df0cb07865a4da2fbbdf5e@167.235.243.27:26656,e0221f9dea312f1cabe53c36f3eec605ac05d953@95.217.191.74:60956,7b2686cb07c742b0d266c25e043054e95f4cc2c0@65.108.235.107:41656,3511b4bffe4d804065181625b32e2507934fdb05@82.208.20.137:26656,c6dcaf5c1d59c696a5b93f53cc5a855b2399f09c@149.102.146.49:26656,6d36c85a0fc1d737906f47af2e090734e0f6d4a3@86.48.3.99:26656,0ae35c02d8b76de9e8af1ec27df2aa446485c774@167.86.94.71:26656,b7a2ef504e66b006ff29857fd85f1da4a40716d2@5.161.78.112:26656,4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,5c08a5f53bf1984dcb5e2a461027c8f847302c9c@80.79.5.162:26656,5191b57c1bd202df86b67b9c7538efcf9e5c0c2a@135.181.89.99:15656,228a33332d579dc6aff1b79dad9f58faa04b1eb2@34.170.240.35:26656,3a754aae8ee42a678b34a4393ff5bb658e43815e@137.184.165.200:41656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
