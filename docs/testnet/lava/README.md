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

**live-peers** (32)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,bbf1fd8b2b993dd354453f90749bd08d108b5de3@194.61.28.30:16656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,fd8ea335ddad4a793d9dbbd9b3b70ec99d6a3331@161.97.139.208:26656,fb2b9d41678f3d1c9c0bdef1a87f2037b6b0088a@146.19.24.252:26666,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,0325a40dfa74c462cc51e64f1c5e331dff1cae2c@65.109.111.159:38656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,abbad4acf9360b250764ef660b5a25a4ec58245f@172.104.159.69:55676,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,0322670e17a172f25fec71f274f2bd28d1b7e74f@185.163.64.143:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,22bd49cb251e649816d2cb6f24897dd2b4602dc4@149.102.157.34:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,c58181fa2022022a36ddda08b79c5b666cb45a7d@194.34.232.225:17656,c19965fe8a1ea3391d61d09cf589bca0781d29fd@162.19.217.52:26656,a20e24a251c9e6325a7c1e05d6a479bcd9c721ac@168.119.52.60:26656,942ca9d454ff241806e40e466533bf4ad1235eaa@46.4.53.208:36656,f8b7dbce90a7cd73f008ce65218caad40c0f56c6@167.86.115.153:32656,d3a466c4892943059b6b361e63eb0665ead5c574@147.135.222.170:55676,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,31550f0ec97d7148b2dae0de2a02240f88d1cfcf@85.114.134.219:12656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
