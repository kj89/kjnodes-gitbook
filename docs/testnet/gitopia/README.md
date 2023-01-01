# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


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

**live-peers** (35)
```
peers="c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,d60ca873fcafca89988ae16958a25748ca3dc42a@128.199.175.106:41656,f3289c45d545c589a4114aeeb364fa4c6fde08d9@109.123.254.216:26656,9c265cb98c21d6748822ca2bed0accacdd8449db@38.242.205.25:26656,231ded997a112e8778afed3fd07ed7b98e0686e0@167.86.91.80:26656,8335a6276710a751f762c31ed4088848f54cc4c3@95.216.215.151:10656,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,996e783f3df1e83e0886eac6c7dc4af451e87fc5@95.165.89.222:24136,c5fa8b2df54c71b7a6479d9ba67dcd87b7109f25@103.104.75.230:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,3bcba60fe08bb6ce59abc19b84cf58e7c915e0ed@193.46.243.243:656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,11127c4ae21201891acc51a14bfc2bcdda292282@164.92.91.63:26656,33196fb0090d2de3671e36545d3425f641c9c0dc@65.109.70.4:41656,74a4bbfbf4d1ca9852d10f3a97e4d012c62aec9e@146.190.102.111:41656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,bbc6a1e115185d5bffcbbf5520dca1c3d626e599@109.123.255.50:26656,5c58d5c43b0a93a28da0cd528af7921567a43921@146.190.34.12:41656,ad7f18fc2b6f28e9c10e888a623f45639f670a4b@159.223.199.25:41656,3727a897b2255c8a2872223af6eb3b9a36d97829@38.242.134.10:10656,165c6969e40fa2ae2340d8e9fa79a14589a46406@185.193.66.202:26656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,4210af79e9137b8647174c003b6b329caaa8e3da@95.217.85.254:15609,af44ee207881ea315ded748adf2c461cde5fa792@143.198.138.43:41656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,ff370fc73f2d80e7107008020971bb274682fddd@128.199.95.198:26656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,7cf64db397849b19f725c3313fb580cec7f95ebf@137.184.42.142:41656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
