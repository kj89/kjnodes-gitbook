# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.8.1 | **Wasm**: OFF

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

**live-peers** (27)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,32d0eaa31ab8f9c2779ce9272b7a68f3d15a8e6e@213.239.207.175:40656,a0476bc75ad2ade9ce8a6b2cd41ef646d3a2e3ee@85.10.193.246:28656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,704db28ae8082ed936675e8eea9b5a71ba946241@18.212.181.61:26656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,7cc7f08ed7ace1a78e6b56c40b8c1bac11f07d2d@94.41.17.212:46656,bdd82a213650291fa7130ab04d21ac07086ecd83@168.119.133.142:26656,bfe46a09c95fd41b139135d962b10e813342a14e@93.92.205.218:26656,5da0681857f4b798a42c11cb036286f7331979cf@86.111.48.184:26656,c46da48bd076586ed28879f4048c592bbb8f88b6@192.9.134.157:26656,d894084a12a25fac29f8296e20bf4c8f60da36eb@89.252.21.37:36656,2e5ab5fc9ebf84aa2d2e5c707461e3ad0d59da80@146.19.24.242:26656,cef0f0ede6c5bc536e45e7151efb06ccfe71cac5@116.203.236.178:26656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,a2e229bcc7fcd1b20bafe33f0c7ec8c1ed0167fa@46.4.53.209:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
