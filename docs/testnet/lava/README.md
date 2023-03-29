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

**live-peers** (40)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,fd8ea335ddad4a793d9dbbd9b3b70ec99d6a3331@161.97.139.208:26656,0516c4d11552b334a683bdb4410fa22ef7e3f8ba@65.21.239.60:11656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,915bd8b97085778b381fe05c0354532203d8618f@65.21.200.54:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,8cd81b9119e4aa45fe549dd12543de862457c989@38.242.155.47:26656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,ac7cefeff026e1c616035a49f3b00c78da63c2e9@18.215.128.248:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,71fb615c968e6ea9458d065d71d47dd1bb10d11e@185.205.246.203:36656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,aebbf38433cc38ed3aad0bb5f2aa567797df78da@46.8.210.144:26756,525696e557db51c4d5f5bca1d7152753c7426c2e@34.192.150.110:26656,7adc61737172235479b405f61477a02be635fb21@62.171.188.69:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,0561fed6e88f2167979e379436529861527d859d@65.109.92.148:61256,435384a91c499443c63a944ea2b3a0f55f8a8c00@161.97.113.41:28656,51f74e630050571b20f490bd47ad155a7f219cbb@173.249.54.227:29656,8ffa4dbef4c0b2a1dc1172760914e2df1468fb22@178.63.8.245:60756,dc1c37e340a191ac0eea7c561b4a3c8fba2ce80a@65.21.237.241:26656,d9703df8c0e5eef6c0766217d611a13ed6ee8d95@88.99.33.248:26656,1f704611e8aa4a53504fac1b80eb55c876dae8bd@65.108.13.154:30656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,64df498c92b9ccaf78012229d399aa34a014f087@65.109.122.105:56659,47385d0a7051109de5342e3b27890c4a4b9e0763@65.108.72.233:16656,fe1998168f5336811a79fbcaf2d5d5a69f2f9f63@65.108.81.145:26656,07c557b393b235a7b004a4a32831e54092dc24a0@91.107.147.250:26656,67dae0d05a857065afd0286d134cbed1c8e9de40@38.242.231.22:29656,0b26d8de77ef75a953976bda222bd077090ddd5a@65.108.133.100:26656,b05087fe1d35652de94643a229d53f8fef9c19e2@5.189.128.140:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
