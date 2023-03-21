# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (35)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,f762b211ee317e8cae9f8ca8cd17a1de1e87f0df@116.202.8.211:20656,0eb2dba8e99f29941edaf58974f469635479562f@154.12.245.39:28656,abbad4acf9360b250764ef660b5a25a4ec58245f@172.104.159.69:55676,f30d07170a092f82702e3c12334fa9fd828b71c6@168.119.124.130:47656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,39309f1ce3d7b6acf9714c749b67c7db6d3f615d@38.242.152.174:26656,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,d5f51ff7adf797e7e4be5f303e75686f6d277886@213.239.207.165:29556,20c13bd0d972acba5588493fb528b558a0317013@38.242.133.203:26656,2e5ab5fc9ebf84aa2d2e5c707461e3ad0d59da80@146.19.24.242:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,90451ff8f47b8f4b077e95837f112135fea14531@207.180.231.123:31656,d7c350f9b16111f04a5fe391ec8ccbed5faee56e@86.48.1.218:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,8cc0e66889c214d721e3fb34083da4c1edafa8ed@65.109.225.86:36656,e232ba0d11839944d92b9035ef98445a0fb94c9f@95.214.53.37:12656,b809d6613bfaca07bf4b3ce9e0a17970efc9b42d@155.248.205.169:26656,fcd5a8f4aebc4c7100573914b7974a35cd389963@5.9.69.253:20656,fdc3bd914360b1be8ee2e9f4a447223830527497@78.46.36.203:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
