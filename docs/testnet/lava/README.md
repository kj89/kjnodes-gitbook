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

**live-peers** (38)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,c58181fa2022022a36ddda08b79c5b666cb45a7d@194.34.232.225:17656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,22bd49cb251e649816d2cb6f24897dd2b4602dc4@149.102.157.34:26656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,bbf1fd8b2b993dd354453f90749bd08d108b5de3@194.61.28.30:16656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,fd8ea335ddad4a793d9dbbd9b3b70ec99d6a3331@161.97.139.208:26656,0d08a1b452e6d7ccdfbc9b54658b5f9ed24eff7b@135.181.138.160:29956,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,b36a39d183383fa068f0db145b179bf8455a06f4@38.242.159.214:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,dced9544a6a8529980dee3ef5b40a251ef06b763@157.97.108.38:20656,c19965fe8a1ea3391d61d09cf589bca0781d29fd@162.19.217.52:26656,ba78f0ac713d5e7a0274ef593674dae337aabbee@176.103.222.18:26656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,d3a466c4892943059b6b361e63eb0665ead5c574@147.135.222.170:55676,b4d53b1e7a2fee2192a30e411ba83136c07ab595@161.97.147.107:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,eae100ae0ee39e01296fe134c80e366a0cecf605@65.109.117.23:44656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,fdc3bd914360b1be8ee2e9f4a447223830527497@78.46.36.203:26656,ac99b8d7f3d863baa09cf6378057b78c4f02d029@91.233.173.45:26656,dd39aa607ab19d57a12fb71e7a5df36cef8d3405@185.48.24.106:26656,5bdbd9a68d212ec341c781cc553043486ce5b8ee@31.220.76.135:26656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,0df9cc98fd8e88920efd02425292813108e14a45@185.202.238.214:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
