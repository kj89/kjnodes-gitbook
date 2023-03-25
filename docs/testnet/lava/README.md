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

**live-peers** (34)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,99327e5cf0f31ac3bb1ca8e39cc9f17c823b7ec1@109.236.88.8:26656,0eb2dba8e99f29941edaf58974f469635479562f@154.12.245.39:28656,6b1d0465b3e2a32b5328e59eb75c38d88233b56f@80.82.215.19:60656,e0f25590f8074b4ea70f069f9be332b19f81f344@23.88.70.109:15656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,0b26d8de77ef75a953976bda222bd077090ddd5a@65.108.133.100:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,0efa60456219f5b7847ee21439aa8662c0a8e1b6@65.21.195.40:26056,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,e5f324d671e8bba44cd8eef2cb5b6e46ccf4f95a@65.108.199.120:60756,f0501090b870f7796dfdd1f1f5479aec2baecfe8@88.198.52.89:11656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@65.109.15.19:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,67ba50d49201090cb09c4d03be2c8db50be2f437@95.217.167.118:26656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,91c02af6333972f222570a73f51feccda8a3ccf1@65.109.93.58:26656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,fdc3bd914360b1be8ee2e9f4a447223830527497@78.46.36.203:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
