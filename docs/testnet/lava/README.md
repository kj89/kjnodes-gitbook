# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)




## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

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

**live-peers** (34)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,4f97a7b7d386dc6cc4b4a7239cf76be3c507a1c8@173.212.243.149:26656,c44a02dba51e23ac06b006fb1285988c89051ce7@85.10.198.171:26556,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,e06519a36d7c780af9ad2be69616a98445112c7a@80.79.5.171:29656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,a724b94c593241890022e204e0065d8baa67168c@116.202.227.117:44656,ef6e9620807e7e4614fd8e02722f8075ec277544@199.175.98.122:26656,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,3693ea5a8a9c0590440a7d6c9a98a022ce3b2455@65.109.92.79:20656,d6a116d2aed64bd2f383b894e38f2a62232e44b7@116.202.161.165:36656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,60be50fae1525143ea9226eff17830c4a474af6c@154.53.39.80:26656,32d0eaa31ab8f9c2779ce9272b7a68f3d15a8e6e@213.239.207.175:40656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,f762b211ee317e8cae9f8ca8cd17a1de1e87f0df@116.202.8.211:20656,bf7aef75c35725f89f31c12197100a1dd91b3174@146.190.47.103:26656,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,f6a3fcd1910ab808192c4c40a29fa0e85cd874cd@52.18.46.103:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,8b774eabd1b4fbffdf9d14fba3d4a1690c69d0ad@65.109.24.227:30656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:33256,14110234a060fc0d9568fb43a32c8b6b0f0f8cc2@65.108.240.151:26656,fdc3bd914360b1be8ee2e9f4a447223830527497@78.46.36.203:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
