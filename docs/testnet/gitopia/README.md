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
peers="9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,c865b9d2e12a2388746aa69dda076db984e74c3f@104.248.249.197:26656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,f9b892ea2e8ed8aa83f7b98e7e47371c23b01924@213.239.207.175:36656,1fee6e7fd077911abab93739f6bf13c62dedbf20@178.62.204.49:26656,c0e48b5f3ab79c24f1594f5a0d67a7a3f717882a@91.223.3.144:26456,61d2b313e2adc9d7990944f8ab5a6f9ecf08084f@65.21.122.171:16656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,921348b18868c83bfc5375fc9860bb28aaaf0d0e@38.242.238.229:26656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,09538ba6159f454a17d76501c59e23bad6fc9d3d@85.190.246.67:26656,3bcba60fe08bb6ce59abc19b84cf58e7c915e0ed@193.46.243.243:656,ad33cf22f96e43448798686ed0f7428b8fdacf5b@5.161.90.174:656,c5135fa9a85fed11a54395df5d5df3c4262d99f1@185.245.183.241:26656,6ce7f9ea8e3019c50057f4eb2a0ed55e8eedf874@194.50.0.44:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,996e783f3df1e83e0886eac6c7dc4af451e87fc5@95.165.89.222:24136,2f0484f05aa2d58d91aa21ea7cb9ce81c2e207ea@85.239.240.187:26656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,74172b8befdca6a86ea200f764c343aa71aff792@178.62.120.239:656,04a4a968f62223ba4a4c498551e89cb8408008be@149.102.152.103:41656,0d9ac8fe7f638dab077fcc448061685f168c0600@146.190.57.222:26656,926b47f8d786e544ec3a9200c61b5b04729a9d57@199.175.98.127:41656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,be9e23be59ab8c9fa5cdde380264f8cab888140c@165.227.38.130:26656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,74a4bbfbf4d1ca9852d10f3a97e4d012c62aec9e@146.190.102.111:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
