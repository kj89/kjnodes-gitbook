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

**live-peers** (29)
```bash
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,07c557b393b235a7b004a4a32831e54092dc24a0@91.107.147.250:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,4f97a7b7d386dc6cc4b4a7239cf76be3c507a1c8@173.212.243.149:26656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,5e068fccd370b2f2e5ab4240a304323af6385f1f@172.93.110.154:27656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,82c3a20fbc0d18b0982b183fb535eee7e03a72c9@207.180.248.217:28656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,32d0eaa31ab8f9c2779ce9272b7a68f3d15a8e6e@213.239.207.175:40656,38093a87129f828125be65e8969bb7ede682b26c@38.242.197.134:26656,122d58154d797c90323bb5424015136275bd98bf@135.181.90.135:26656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656,7fb838681ff9855a634c7823de605fb4a5d22eba@65.108.144.202:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,df4a126e75dac4e7e2c4c7ea451a547c337a9f2a@46.4.253.147:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,75ed1e87b48d6e1ab341e3568708c9fb81743ffa@65.109.88.251:11036,c40182c2efc94ea0f3e97995f9e16259a6d51fdd@18.184.167.46:26656,a2e229bcc7fcd1b20bafe33f0c7ec8c1ed0167fa@46.4.53.209:36656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,2e5ab5fc9ebf84aa2d2e5c707461e3ad0d59da80@146.19.24.242:26656,53cba364b17674a182a19bd0fd6fc06ffae488b0@161.97.133.186:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
